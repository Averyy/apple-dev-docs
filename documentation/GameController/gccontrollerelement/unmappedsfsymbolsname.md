# unmappedSfSymbolsName

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The element’s system symbol, not the remapped symbol.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var unmappedSfSymbolsName: String? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSString * unmappedSfSymbolsName;
```

## Discussion

Use this property to get the original unmapped name. Otherwise, use the [`sfSymbolsName`](./sfsymbolsname.md) property to get the possibly remapped symbol.

## See Also

### Displaying a symbol
- [var sfSymbolsName: String?](./sfsymbolsname.md)
  A system symbol for the element or the remapped element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/unmappedsfsymbolsname)*