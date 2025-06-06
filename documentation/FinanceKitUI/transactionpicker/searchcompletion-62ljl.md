# searchCompletion(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Associates a fully formed string with the value of this view when used as a search suggestion.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func searchCompletion(_ completion: String) -> some View
```

#### Discussion

Use this method to associate a fully formed string with a view that is within a search suggestion list context. The system uses this value when the view is selected to replace the partial text being currently edited of the associated search field.

On tvOS, the string that you provide to the this modifier is used when displaying the associated suggestion and when replacing the partial text of the search field.

```None
SearchPlaceholderView()
    .searchable(text: $text) {
        Text("🍎").searchCompletion("apple")
        Text("🍐").searchCompletion("pear")
        Text("🍌").searchCompletion("banana")
    }
```

## Parameters

- `text`: A string to use as the view’s completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/searchcompletion(_:)-62ljl)*