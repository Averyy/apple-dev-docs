# Displaying data in lists

**Framework**: SwiftUI

Visualize collections of data with platform-appropriate appearance.

#### Overview

Displaying a collection of data in a vertical list is a common requirement in many apps. Whether it’s a list of contacts, a schedule of events, an index of categories, or a shopping list, you’ll often find a use for a [`List`](list.md).

List views display collections of items vertically, load rows as needed, and add scrolling when the rows don’t fit on the screen, making them suitable for displaying large collections of data.

By default, list views also apply platform-appropriate styling to their elements. For example, on iOS, the default configuration of a list displays a separator line between each row, and adds disclosure indicators next to items that initiate navigation actions.

> **Note**: If you want to remove the platform-appropriate styling — such as row separators or automatic disclosure indicators — from your list, consider using [`LazyVStack`](lazyvstack.md) instead. For more information on working with lazy stacks, see [`Creating performant scrollable stacks`](creating-performant-scrollable-stacks.md)

The code in this article shows the use of list views to display a company’s staff directory. Each section enhances the usefulness of the list, by adding custom cells, splitting the list into sections, and using the list selection to navigate to a detail view.

##### Prepare Your Data for Iteration

The most common use of [`List`](list.md) is for representing collections of information in your data model. The following example defines a `Person` as an [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) type with the properties `name` and `phoneNumber`. An array called `staff` contains two instances of this type.

```swift
struct Person: Identifiable {
     let id = UUID()
     var name: String
     var phoneNumber: String
 }

var staff = [
    Person(name: "Juan Chavez", phoneNumber: "(408) 555-4301"),
    Person(name: "Mei Chen", phoneNumber: "(919) 555-2481")
]
```

To present the contents of the array as a list, the example creates a `List` instance. The list’s content builder uses a [`ForEach`](foreach.md) to iterate over the `staff` array. For each member of the array, the listing creates a row view by instantiating a new [`Text`](text.md) that contains the name of the `Person`.

```swift
struct StaffList: View {
    var body: some View {
        List {
            ForEach(staff) { person in
                Text(person.name)
            }
        }
    }
}
```

![A screenshot of a list view, showing a vertical list with two text entries: Juan Chavez and Mei Chen.](https://docs-assets.developer.apple.com/published/6f0312d4cce3f6eb1cc9bfa4b5da3d19/Displaying-Data-in-Lists-plain-cells%402x.png)

Members of a list must be uniquely identifiable from one another. Unique identifiers allow SwiftUI to automatically generate animations for changes in the underlying data, like inserts, deletions, and moves. Identify list members either by using a type that conforms to [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable), as `Person` does, or by providing an `id` parameter with the key path to a unique property of the type. The `ForEach` that populates the list above depends on this behavior, as do the `List` initializers that take a [`RandomAccessCollection`](https://developer.apple.com/documentation/Swift/RandomAccessCollection) of members to iterate over.

> ❗ **Important**: The values you use for [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) data must be unique. Using a [`UUID`](https://developer.apple.com/documentation/Foundation/UUID) or a database row identifier are both good choices, whereas using data like a person’s name or phone number could potentially contain duplicates.

##### Display Data Inside a Row

Each row inside a [`List`](list.md) must be a SwiftUI [`View`](view.md). You may be able to represent your data with a single view such as an [`Image`](image.md) or [`Text`](text.md) view, or you may need to define a custom view to compose several views into something more complex.

As your row views get more sophisticated, refactor the views into separate view structures, passing in the data that the row needs to render. The following example defines a `PersonRowView` to create a two-line view for a `Person`, using fonts, colors, and the system “phone” icon image to visually style the data.

```swift
struct PersonRowView: View {
    var person: Person

    var body: some View {
        VStack(alignment: .leading, spacing: 3) {
            Text(person.name)
                .foregroundColor(.primary)
                .font(.headline)
            HStack(spacing: 3) {
                Label(person.phoneNumber, systemImage: "phone")
            }
            .foregroundColor(.secondary)
            .font(.subheadline)
        }
    }
}

struct StaffList: View {
    var body: some View {
        List {
            ForEach(staff) { person in
                PersonRowView(person: person)
            }
        }
    }
}
```

![A list with two entries, each showing a name and phone number. Each list item has a two-line cell. The first line shows the name in bold. The second shows a phone icon, followed by the phone number with a plain font and a lighter color.](https://docs-assets.developer.apple.com/published/e76d2de5a5a5a38be79930b59304fa6c/Displaying-Data-in-Lists-custom-cells%402x.png)

For more information on composing the types of views commonly used inside list rows, see [`Building layouts with stack views`](building-layouts-with-stack-views.md).

##### Represent Data Hierarchy with Sections

[`List`](list.md) views can also display data with a level of hierarchy, grouping associated data into sections.

Consider an expanded data model that represents an entire company, including multiple departments. Each `Department` has a name and an array of `Person` instances, and the company has an array of the `Department` type.

```swift
struct Department: Identifiable {
    let id = UUID()
    var name: String
    var staff: [Person]
}

struct Company {
    var departments: [Department]
}

var company = Company(departments: [
    Department(name: "Sales", staff: [
        Person(name: "Juan Chavez", phoneNumber: "(408) 555-4301"),
        Person(name: "Mei Chen", phoneNumber: "(919) 555-2481"),
        // ...
    ]),
    Department(name: "Engineering", staff: [
        Person(name: "Bill James", phoneNumber: "(408) 555-4450"),
        Person(name: "Anne Johnson", phoneNumber: "(417) 555-9311"),
        // ...
    ]),
    // ...
])
```

Use [`Section`](section.md) views to give the data inside a `List` a level of hierarchy. Start by creating the `List`, using a [`ForEach`](foreach.md) to iterate over the `company.departments` array, and then create `Section` views for each department. Within the section’s view builder, use a `ForEach` to iterate over the department’s `staff`, and return a customized view for each `Person`.

```swift
List {
     ForEach(company.departments) { department in
         Section(header: Text(department.name)) {
             ForEach(department.staff) { person in
                PersonRowView(person: person)
             }
         }
     }
 }
```

![A list with sections. The first has a section header with the title Sales, followed by four person entries as individual rows in this section. The next section, Engineering, contains four entries, followed by Customer Service with two entries.](https://docs-assets.developer.apple.com/published/49a2043284fb273a8f09b74a0f02d82b/Displaying-Data-in-Lists-sections%402x.png)

> **Note**: If your data hierarchy is too deep to represent with a single level of sections and rows, [`OutlineGroup`](outlinegroup.md) and [`DisclosureGroup`](disclosuregroup.md) might be a better fit. These views use a disclosure metaphor to allow the user to drill down to an arbitrary depth in the hierarchy.

#### Use Lists for Navigation

Using a [`NavigationLink`](navigationlink.md) within a [`List`](list.md) contained inside a [`NavigationView`](navigationview.md) adds platform-appropriate visual styling, and in some cases, additional container views that provide the structure for navigation. SwiftUI uses one of two visual presentations, based on the runtime environment:

- A list with disclosure indicators, which performs an animated navigation to a destination scene when the user chooses a list item. SwiftUI uses this presentation on watchOS, tvOS, and on most iOS devices except as described below.
- A two-panel split view, with the top-level data as a list on the left side and the detail on the right. To get this presentation, you also need to provide a placeholder view after the list; this placeholder fills the detail pane until the user makes a selection. SwiftUI uses this two-panel approach on macOS, iPadOS, and on iOS devices with sufficient horizontal space, as indicated by the [`horizontalSizeClass`](environmentvalues/horizontalsizeclass.md) environment value.

The following example sets up a navigation-based UI by wrapping the list with a navigation view. Instances of `NavigationLink` wrap the list’s rows to provide a `destination` view to navigate to when the user taps the row. If a split view navigation is appropriate for the platform, the right panel initially contains the “No Selection” placeholder view, which the navigation view replaces with the destination view when the user makes a selection.

```swift
NavigationView {
    List {
        ForEach(company.departments) { department in
            Section(header: Text(department.name)) {
                ForEach(department.staff) { person in
                    NavigationLink(destination: PersonDetailView(person: person)) {
                        PersonRowView(person: person)
                    }
                }
            }
        }
    }
    .navigationTitle("Staff Directory")

    // Placeholder
    Text("No Selection")
        .font(.headline)
}
```

In this example, the view passed in as the `destination` is a `PersonDetailView`, which repeats the information from the list. In a more complex app, this detail view could show more information about a `Person` than would fit inside the list row.

```swift
struct PersonDetailView: View {
    var person: Person

    var body: some View {
        VStack {
            Text(person.name)
                .foregroundColor(.primary)
                .font(.title)
                .padding()
            HStack {
                Label(person.phoneNumber, systemImage: "phone")
            }
            .foregroundColor(.secondary)
        }
    }
}
```

On most iOS devices (those with a compact horizontal size class), the list appears as a view by itself, and tapping a row performs an animated transition to the destination view. The following figure shows both the list view and the destination view that appears when the user makes a selection:

![Two iOS views in a before-and-after arrangement. First, the title Staff Directory and a list of employees, separated into sections, with the row named Juan Chavez selected. Second, a detail view showing the name Juan Chavez and his phone number.](https://docs-assets.developer.apple.com/published/917e6451b68cf86a99b18a71c06b6feb/Displaying-Data-in-Lists-navigation-iOS%402x.png)

On the other hand, iPadOS and macOS show the list and the detail view together as a multi-column view. The following figure shows what this example looks like on macOS prior to making a selection, which means the “No selection” placeholder view is still in the detail column.

![A macOS window titled Staff Directory, with a narrow column on the left that shows a list of employees grouped into sections by department. The right column shows a text view that reads No selection.](https://docs-assets.developer.apple.com/published/41db282f034c09e59b6cd5e22d14d859/Displaying-Data-in-Lists-navigation-macOS%402x.png)

You can use the [`navigationViewStyle(_:)`](view/navigationviewstyle(_:).md) view modifier to change the default behavior of a `NavigationView`. For example, on iOS, the [`StackNavigationViewStyle`](stacknavigationviewstyle.md) forces single-column mode, even on an iPad in landscape orientation.

## See Also

- [struct List](list.md)
  A container that presents rows of data arranged in a single column, optionally providing the ability to select one or more members.
- [func listStyle<S>(S) -> some View](view/liststyle(_:).md)
  Sets the style for lists within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/displaying-data-in-lists)*