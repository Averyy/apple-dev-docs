# device

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The Metal device object that created the library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

```objc
@property (readonly) id<MTLDevice> device;
```

#### Discussion

You can only use the library with this [`MTLDevice`](../mtldevice.md).

## See Also

### Identifying the library
- [var label: String?](./label.md)
  A string that identifies the library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibrary/device)*