# localizedDescription

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A longer form of the pass description that the system displays on the sharing sheet.

**Availability**:
- iOS 14.0+ - Deprecated in 16.0
- iPadOS 14.0+ - Deprecated in 16.0
- Mac Catalyst 14.0+ - Deprecated in 16.0
- macOS
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var localizedDescription: String { get }
```

```objc
@property (nonatomic, strong, readonly) NSString * localizedDescription;
```

#### Discussion

This property isn’t used and currently contains an empty string.

## See Also

### Displaying information on the share sheet
- [var ownerDisplayName: String](./ownerdisplayname.md)
  The name of the person that receives a shared pass.
- [var passThumbnailImage: CGImage](./passthumbnailimage.md)
  A thumbnail image of a pass that the system displays on the sharing sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkshareablepassmetadata/localizeddescription)*