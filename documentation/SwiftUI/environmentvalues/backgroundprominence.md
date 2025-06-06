# backgroundProminence

**Framework**: SwiftUI  
**Kind**: property

The prominence of the background underneath views associated with this environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var backgroundProminence: BackgroundProminence { get set }
```

#### Discussion

Foreground elements above an increased prominence background are typically adjusted to have higher contrast against a potentially vivid color, such as taking on a higher opacity monochrome appearance according to the `colorScheme`. System styles like `primary`, `secondary`, etc will automatically resolve to an appropriate style in this context. The property can be read and used for custom styled elements.

In the example below, a custom star rating element is in a list row alongside some text. When the row is selected and has an increased prominence appearance, the text and star rating will update their appearance, the star rating replacing its use of yellow with the standard `secondary` style.

```swift
struct RecipeList: View {
    var recipes: [Recipe]
    @Binding var selectedRecipe: Recipe.ID?

    var body: some View {
        List(recipes, selection: $selectedRecipe) {
            RecipeListRow(recipe: $0)
        }
    }
}

struct RecipeListRow: View {
    var recipe: Recipe
    var body: some View {
        VStack(alignment: .leading) {
            HStack(alignment: .firstTextBaseline) {
                Text(recipe.name)
                Spacer()
                StarRating(rating: recipe.rating)
            }
            Text(recipe.description)
                .foregroundStyle(.secondary)
                .lineLimit(2, reservesSpace: true)
        }
    }
}

private struct StarRating: View {
    var rating: Int

    @Environment(\.backgroundProminence)
    private var backgroundProminence

    var body: some View {
        HStack(spacing: 1) {
            ForEach(0..<rating, id: \.self) { _ in
                Image(systemName: "star.fill")
            }
        }
        .foregroundStyle(backgroundProminence == .increased ?
            AnyShapeStyle(.secondary) : AnyShapeStyle(.yellow))
        .imageScale(.small)
    }
}
```

Note that the use of `backgroundProminence` was used by a view that was nested in additional stack containers within the row. This ensured that the value correctly reflected the environment within the list row itself, as opposed to the environment of the list as a whole. One way to ensure correct resolution would be to prefer using this in a custom ShapeStyle instead, for example:

```swift
private struct StarRating: View {
    var rating: Int

    var body: some View {
        HStack(spacing: 1) {
            ForEach(0..<rating, id: \.self) { _ in
                Image(systemName: "star.fill")
            }
        }
        .foregroundStyle(FillStyle())
        .imageScale(.small)
    }
}

extension StarRating {
    struct FillStyle: ShapeStyle {
        func resolve(in env: EnvironmentValues) -> some ShapeStyle {
            switch env.backgroundProminence {
            case .increased: return AnyShapeStyle(.secondary)
            default: return AnyShapeStyle(.yellow)
            }
        }
    }
}
```

Views like `List` and `Table` as well as standard shape styles like `ShapeStyle.selection` will automatically update the background prominence of foreground views. For custom backgrounds, this environment property can be explicitly set on views above custom backgrounds.

## See Also

- [func listRowBackground<V>(V?) -> some View](view/listrowbackground(_:).md)
  Places a custom background view behind a list row item.
- [func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some View](view/alternatingrowbackgrounds(_:).md)
  Overrides whether lists and tables in this view have alternating row backgrounds.
- [struct AlternatingRowBackgroundBehavior](alternatingrowbackgroundbehavior.md)
  The styling of views with respect to alternating row backgrounds.
- [struct BackgroundProminence](backgroundprominence.md)
  The prominence of backgrounds underneath other views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/backgroundprominence)*