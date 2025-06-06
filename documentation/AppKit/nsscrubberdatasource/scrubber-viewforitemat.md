# scrubber(_:viewForItemAt:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Asks the data source object for the view the corresponds to the specified item in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func scrubber(_ scrubber: NSScrubber, viewForItemAt index: Int) -> NSScrubberItemView
```

#### Return Value

A configured item view object.

## Parameters

- `scrubber`: The scrubber requesting the view.
- `index`: The index that specifies the location of the item in the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberdatasource/scrubber(_:viewforitemat:))*