# setItemProviders(_:localOnly:expirationDate:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets and configures an explicit array of item providers for the pasteboard.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setItemProviders(_ itemProviders: [NSItemProvider], localOnly: Bool, expirationDate: Date?)
```

```objc
- (void) setItemProviders:(NSArray<NSItemProvider *> *) itemProviders localOnly:(BOOL) localOnly expirationDate:(NSDate *) expirationDate;
```

## Parameters

- `itemProviders`: An array of item providers for the pasteboard.
- `localOnly`: If [`false`](../../Swift/false.md), the pasteboard items are available to other devices through the Handoff feature; if [`true`](../../Swift/true.md), the pasteboard items are only available to the local device.
- `expirationDate`: An [`NSDate`](../../Foundation/nsdate.md) value that specifies the time and date that you want the system to remove the pasteboard items from the pasteboard.

## See Also

### Getting and setting item providers
- [var itemProviders: [NSItemProvider]](./itemproviders.md)
  An array of item providers for the pasteboard.
- [func setObjects([any NSItemProviderWriting])](./setobjects%28_%29-lljo.md)
  Sets an array of item providers for the pasteboard, based on a specified array of objects.
- [func setObjects<T>([T])](./setobjects%28_%29-fjg8.md)
  Sets an array of item providers for the pasteboard, based on a specified array of objects.
- [func setObjects([any NSItemProviderWriting], localOnly: Bool, expirationDate: Date?)](./setobjects%28_,localonly,expirationdate%29-3h3iz.md)
  Sets and configures an array of item providers for the pasteboard, based on a specified array of objects.
- [func setObjects<T>([T], localOnly: Bool, expirationDate: Date?)](./setobjects%28_,localonly,expirationdate%29-26u8o.md)
  Sets and configures an array of item providers for the pasteboard, based on a specified array of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/setitemproviders(_:localonly:expirationdate:))*