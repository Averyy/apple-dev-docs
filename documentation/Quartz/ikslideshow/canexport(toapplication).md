# canExport(toApplication:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Type Method

Finds out whether the slideshow can export its contents to an application.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func canExport(toApplication applicationBundleIdentifier: String!) -> Bool
```

```objc
+ (BOOL) canExportToApplication:(NSString *) applicationBundleIdentifier;
```

#### Return Value

[`true`](../../Swift/true.md) if the slideshow can be exported to the specified application; [`false`](../../Swift/false.md) otherwise.

## Parameters

- `applicationBundleIdentifier`: The bundle identifier of the application that you want to export the slideshow to. See [Bundle Identifiers](../bundle-identifiers.md).

## See Also

### Exporting Slideshow Items
- [class func exportItem(Any!, toApplication: String!)](./exportitem%28_,toapplication%29.md)
  Exports a slideshow item to the application that has the provided bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshow/canexport(toapplication:))*