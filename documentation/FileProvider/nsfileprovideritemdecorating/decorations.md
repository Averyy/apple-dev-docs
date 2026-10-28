# decorations

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Asks the item for an array of decorations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var decorations: [NSFileProviderItemDecorationIdentifier]? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSArray<NSString *> * decorations;
```

## Discussion

The system calls this method to request the item’s decorations. Your implementation should return an array of [`NSFileProviderItemDecorationIdentifier`](../nsfileprovideritemdecorationidentifier.md) instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemdecorating/decorations)*