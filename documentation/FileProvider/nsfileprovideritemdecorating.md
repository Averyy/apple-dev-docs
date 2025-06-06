# NSFileProviderItemDecorating

**Framework**: File Provider  
**Kind**: protocol

Support for decorating items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderItemDecorating : NSFileProviderItemProtocol
```

#### Overview

To adopt this protocol, implement the [`decorations`](nsfileprovideritemdecorating/decorations.md) method for your extension’s [`NSFileProviderItem`](nsfileprovideritem-swift.typealias.md) and return valid identifiers for the desired decorations.

You define decorations in the File Provider extension’s `Info.plist` file by adding the `NSFileProviderDecorations` key to the `NSExtension` dictionary.

```swift
 <key>NSFileProviderDecorations</key>
 <array>
   <dict>
      <key>Identifier</key>
      <string>$(PRODUCT_BUNDLE_IDENTIFIER).hasComments</string>
      <key>BadgeImageType</key>
      <string>com.someone.item.decoration.unreadCommentIcon</string>
      <key>Category</key>
      <string>Badge</string>
      <key>LocalizedTitle</key>
      <dict>
         <key>NSStringFormat</key>
         <string>%@ unread comments</string>
         <key>NSStringFormatValues</key>
         <array>
            <string>item.userInfo.unreadCommentCount</string>
         </array>
      </dict>
   </dict>
 </array>
```

Use the following keys to define the decorations:

The `Category` value must be one of the following:

## Topics

### Providing Decorations
- [var decorations: [NSFileProviderItemDecorationIdentifier]?](nsfileprovideritemdecorating/decorations.md)
  Asks the item for an array of decorations.

## Relationships

### Inherits From
- [NSFileProviderItemProtocol](nsfileprovideritemprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct NSFileProviderItemFields](nsfileprovideritemfields.md)
  Fields that specify which of the item’s properties have changed.
- [class NSFileProviderItemVersion](nsfileprovideritemversion.md)
  The version of the item’s content and its metadata.
- [class NSFileProviderRequest](nsfileproviderrequest.md)
  An object that provides information about the application requesting data from the File Provider extension.
- [struct NSFileProviderItemDecorationIdentifier](nsfileprovideritemdecorationidentifier.md)
  A decoration identifier defined in the File Provider extension’s information property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemdecorating)*