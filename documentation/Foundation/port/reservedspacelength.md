# reservedSpaceLength

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number of bytes of space reserved by the receiver for sending data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var reservedSpaceLength: Int { get }
```

```objc
@property (readonly) NSUInteger reservedSpaceLength;
```

#### Discussion

The number of bytes reserved by the receiver for sending data. The default length is `0`.

## See Also

### Setting information
- [func send(before: Date, components: NSMutableArray?, from: Port?, reserved: Int) -> Bool](./send%28before,components,from,reserved%29.md)
  This method is provided for subclasses that have custom types of `NSPort`.
- [func send(before: Date, msgid: Int, components: NSMutableArray?, from: Port?, reserved: Int) -> Bool](./send%28before,msgid,components,from,reserved%29.md)
  This method is provided for subclasses that have custom types of `NSPort`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/port/reservedspacelength)*