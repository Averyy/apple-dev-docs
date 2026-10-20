# setObjects(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets an array of item providers for the pasteboard, based on a specified array of objects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setObjects(_ objects: [any NSItemProviderWriting])
```

```objc
- (void) setObjects:(NSArray<id<NSItemProviderWriting>> *) objects;
```

## Parameters

- `objects`: An array of item providers for the pasteboard.

## See Also

### Getting and setting item providers
- [var itemProviders: [NSItemProvider]](./itemproviders.md)
  An array of item providers for the pasteboard.
- [func setItemProviders([NSItemProvider], localOnly: Bool, expirationDate: Date?)](./setitemproviders%28_,localonly,expirationdate%29.md)
  Sets and configures an explicit array of item providers for the pasteboard.
- [func setObjects<T>([T])](./setobjects%28_%29-fjg8.md)
  Sets an array of item providers for the pasteboard, based on a specified array of objects.
- [func setObjects([any NSItemProviderWriting], localOnly: Bool, expirationDate: Date?)](./setobjects%28_,localonly,expirationdate%29-3h3iz.md)
  Sets and configures an array of item providers for the pasteboard, based on a specified array of objects.
- [func setObjects<T>([T], localOnly: Bool, expirationDate: Date?)](./setobjects%28_,localonly,expirationdate%29-26u8o.md)
  Sets and configures an array of item providers for the pasteboard, based on a specified array of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/setobjects(_:)-lljo)*