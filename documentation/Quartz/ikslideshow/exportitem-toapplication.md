# exportItem(_:toApplication:)

**Framework**: Quartz  
**Kind**: method

Exports a slideshow item to the application that has the provided bundle identifier.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func exportItem(_ item: Any!, toApplication applicationBundleIdentifier: String!)
```

## Parameters

- `item`: The item to export
- `applicationBundleIdentifier`: The bundle identifier of the application that you want to export the item to.

## See Also

- [class func canExport(toApplication: String!) -> Bool](ikslideshow/canexport(toapplication:).md)
  Finds out whether the slideshow can export its contents to an application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshow/exportitem(_:toapplication:))*