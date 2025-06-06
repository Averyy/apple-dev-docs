# canExport(toApplication:)

**Framework**: Quartz  
**Kind**: method

Finds out whether the slideshow can export its contents to an application.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func canExport(toApplication applicationBundleIdentifier: String!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the slideshow can be exported to the specified application; [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## Parameters

- `applicationBundleIdentifier`: The bundle identifier of the application that you want to export the slideshow to. See  .

## See Also

- [class func exportItem(Any!, toApplication: String!)](ikslideshow/exportitem(_:toapplication:).md)
  Exports a slideshow item to the application that has the provided bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshow/canexport(toapplication:))*