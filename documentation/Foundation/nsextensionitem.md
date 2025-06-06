# NSExtensionItem

**Framework**: Foundation  
**Kind**: class

An immutable collection of values representing different aspects of an item for an extension to act upon.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSExtensionItem
```

## Topics

### Identifying the Item
- [var attributedTitle: NSAttributedString?](nsextensionitem/attributedtitle.md)
  An optional title for the item.
- [var userInfo: [AnyHashable : Any]?](nsextensionitem/userinfo.md)
  An optional dictionary of keys and values corresponding to the extension item’s properties.
### Item Contents
- [var attachments: [NSItemProvider]?](nsextensionitem/attachments.md)
  An optional array of media data associated with the extension item.
- [var attributedContentText: NSAttributedString?](nsextensionitem/attributedcontenttext.md)
  An optional string describing the extension item content.
### Constants
- [Property Keys](property-keys.md)
  These keys correspond to the extension item properties and are specified in the extension’s `Info.plist`.
- [UTI Subtypes for Data Detector Types](uti-subtypes-for-data-detector-types.md)
  These constants represent sub-Uniform Type Identifier of `com.apple.structured-text`

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

- [class NSItemProvider](nsitemprovider.md)
  An item provider for conveying data or a file between processes during drag-and-drop or copy-and-paste activities, or from a host app to an app extension.
- [Add Functionality to Finder with Action Extensions](../AppKit/add-functionality-to-finder-with-action-extensions.md)
  Implement Action Extensions to provide quick access to commonly used features of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensionitem)*