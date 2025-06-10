# Enhancing your app’s content with tab navigation

**Framework**: SwiftUI

Keep your app content front and center while providing quick access to navigation using the tab bar.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

#### Overview

[`Destination Video`](https://developer.apple.com/documentation/visionOS/destination-video) adopts the [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) tab view style, which optimizes the content browsing experience for each platform.

Starting in iPadOS 18, the tab bar appears on the top of the screen floating over your content instead of appearing at the bottom of the screen. This appearance creates an immersive full-screen browsing experience. Tab bars provide people with access to the top-level navigation in your app. However, too many tabs can make it hard for people to locate content. Implementing a sidebar makes it easier to navigate a detailed information hierarchy.

##### Create a Tab Bar

You can create a [`TabView`](tabview.md) with an explicit selection binding using the [`init(selection:content:)`](tabview/init(selection:content:).md) initializer. To add a tab within a `TabView` initialize a [`Tab`](tab.md). Destination Video uses the [`init(_:systemImage:value:content:)`](tab/init(_:systemimage:value:content:).md) initializer to create each tab:

```swift
@State private var selectedTab: Tabs = .watchNow

var body: some View {
    TabView(selection: $selectedTab) {
        Tab("Watch Now", systemImage: "play", value: .watchNow) {
            WatchNowView()
        }
        // More tabs...
    }
}
```

The selection value type of the `TabView` matches the value type of the tabs it contains. In this case, the value of each `Tab` is of type `Tabs`, which this sample defines the following enumeration:

```swift
enum Tabs: Equatable, Hashable, Identifiable {
    case watchNow
    case library
    case new
    case favorites
    case search
}
```

> **Note**: When using symbol images for your tabs, use the outline variant. The system automatically selects the filled variant when it appears in a tab bar.

![A screenshot of the iPadOS tab bar in Simulator. The tab bar is highlighted, the tab bar has an icon on the left that turns it into a sidebar, followed by the tabs: Watch Now, Library, New, Favorites, and Search, which appears as a magnifying glass.](https://docs-assets.developer.apple.com/published/9a5ad10f868c9474778c59000b7602ec/Enhancing-your-app-content-with-tab-navigation-create-tab%402x.png)

Additionally, this sample uses the [`search`](tabrole/search.md) role with the [`init(value:role:content:)`](tab/init(value:role:content:).md) initializer. Setting the tab role to `search` makes the system applies a few default customizations to the `Tab`. The search tab gets:

- The default title for search, “search”
- The default system symbol for search, a magnifying glass
- The default pinned behavior for search, the system automatically pins it in the tab bar

```swift
Tab(value: .search, role: .search) {
    // ...
}
```

Pinned tabs appear at the trailing edge of the tab bar, depending on the preferred language of your app. When the language is a left-to-right language, they appear on the right side. When the language is a right-to-left language, they’re on the left side.

![A screenshot of the tab bar with the a search tab highlighted.  The tab bar has an icon on the left that turns it into a sidebar, followed by the tabs: Watch Now, Library, New, Favorites, and Search, which appears as a magnifying glass.](https://docs-assets.developer.apple.com/published/59a57fb092b9a75b4ef8c91d81b0986e/Enhancing-your-app-content-with-tab-navigation-search%402x.png)

##### Build Hierarchy in Tab View

You can use a [`TabSection`](tabsection.md) to declare a secondary tab hierarchy within a `TabView`. For example Destination Video uses the [`init(content:header:)`](tabsection/init(content:header:).md) initializer to create tab sections.

```swift
TabView(selection: $selectedTab) {
    Tab("Watch Now", systemImage: "play", value: .watchNow) {
        WatchNowView()
    }

    // More tabs...
    
    TabSection {
        Tab("Cinematic Shots", systemImage: "list.and.film", value: .collections(.cinematic)) {
            // ...
        }
    } header: {
        Label("Collections", systemImage: "folder")
    }
}
```

Then it extends the `Tabs` enumeration to account for secondary tabs:

```swift
enum Tabs: Equatable, Hashable, Identifiable {
    case watchNow
    // ..
    case search
    case collections(Category)
    case animations(Category)
}

enum Category: Equatable, Hashable, Identifiable, CaseIterable {
    case cinematic
    case forest
    case sea
    // ...
}
```

This sample uses a [`ForEach`](foreach.md) loop to iterate and initialize a new `Tab` for each tab value.

```swift
TabSection {
    ForEach(Category.collectionsList) { collection in
        Tab(collection.name, systemImage: collection.icon, value: Tabs.collections(collection)) {
            // ..
        }
    }
} header: {
    Label("Collections", systemImage: "folder")
}
```

##### Make the Tab Bar Adaptable

Tab bars with the [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) style allow people to toggle between the sidebar and tab bar. This lets your app leverage the convenience of being able to quickly navigate to top-level destinations within a compact tab bar while providing rich navigation hierarchy and destination options in the sidebar.

To create an adaptable tab bar, Destination Video adds the [`tabViewStyle(_:)`](view/tabviewstyle(_:).md) modifier to its `TabView` and passes in the value [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md).

```swift
TabView(selection: $selectedTab) {
    // Tabs
    // ..
}
.tabViewStyle(.sidebarAdaptable)

```

A `TabView` with the `sidebarAdaptable` style appears differently depending on the platform, as shown in the following images.

> **Note**: By default, contents in a `ScrollView(.horizontal)` scroll under the sidebar when you use the `sidebarAdaptable` tab view style in iPadOS. You can prevent the content from scrolling under the sidebar by adding the [`clipped(antialiased:)`](view/clipped(antialiased:).md) or [`clipShape(_:style:)`](view/clipshape(_:style:).md) modifier to `ScrollView`.

##### Enable Customization

Tab view customization allows people to enter edit mode and personalize the tab bar. The customization in Destination Video allows people to:

- Drag and drop tabs to remove and add tabs to the tab bar
- Hide non-essential tabs
- Reorder tabs in tab sections in the sidebar
- Reorder tabs in the tab bar

To enable customizations, this sample defines a [`TabViewCustomization`](tabviewcustomization.md) and attaches it to the `TabView` using the [`tabViewCustomization(_:)`](view/tabviewcustomization(_:).md) modifier. To persist the customization, this sample adds [`AppStorage`](appstorage.md) with an identifier for a  `TabViewCustomization` variable. Finally, it adds the [`customizationID(_:)`](tabcontent/customizationid(_:).md) modifier to each tab.

```swift
@AppStorage("sidebarCustomizations") var tabViewCustomization: TabViewCustomization
@State private var selectedTab: Tabs = .watchNow

var body: some View {
    TabView(selection: $selectedTab) {
        Tab("Watch Now", systemImage: "play", value: .watchNow) {
            WatchNowView()
        }
        .customizationID(Tabs.watchNow.customizationID)

        // More tabs...

    }
    .tabViewCustomization($tabViewCustomization)
}
```

To keep the most important tabs visible and in a fixed position, turn off customization behavior for those tabs using the [`customizationBehavior(_:for:)`](tabcontent/customizationbehavior(_:for:).md) modifier.

```swift
Tab("Watch Now", systemImage: "play", value: .watchNow) {
    WatchNowView()
}
.customizationBehavior(.disabled, for: .sidebar, .tabBar)
```

![A screenshot of a tab view in edit mode on iPad.](https://docs-assets.developer.apple.com/published/493112fc30c02a81d5a079a6b7e45a34/Enhancing-your-app-content-with-tab-navigation-customization%402x.png)

##### Set the Default Visibility for Tabs

In iPadOS, if there are too many tabs to fit in the screen, the system collapses the tabs that don’t fit and enables scrolling. However, having too many tabs can make it harder for people to locate the tab they’re looking for and navigate your app. Consider limiting the number of tabs so they all fit in the tab bar. The [`defaultVisibility(_:for:)`](tabcontent/defaultvisibility(_:for:).md) modifier sets the default visibility of a `Tab` or `TabSection`.

Destination Video contains five tabs and two tab sections, each tab section contains multiple secondary tabs, but only seven tabs appear in the tab bar. In order to limit the tab bar to the most important tabs, all tabs within a `TabSection` are hidden from the tab bar by default.

```swift
TabSection {
    // Tabs
} header {
    // Section header
}
.defaultVisibility(.hidden, for: .tabBar)
```

If you enable customization, the [`defaultVisibility(_:for:)`](tabcontent/defaultvisibility(_:for:).md) modifier still allows people to drag a tab from the sidebar into the tab bar. If you want to restrict tabs to only appear in the sidebar use [`sidebarOnly`](tabplacement/sidebaronly.md) instead of setting the default visibility.

For design guidance, see Human Interface Guidelines >  [`Tab bars`](https://developer.apple.com/design/Human-Interface-Guidelines/tab-bars).

###### Related Samples

###### Related Articles

###### Related Videos


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/enhancing-your-app-content-with-tab-navigation)*