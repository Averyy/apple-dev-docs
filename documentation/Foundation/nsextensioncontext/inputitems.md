# inputItems

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The list of input [`NSExtensionItem`](../nsextensionitem.md) objects associated with the context.

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
var inputItems: [Any] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSArray * inputItems;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSArray * inputItems;
```

## Discussion

If the context has no input items, this array is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/inputitems)*