# compositionAttributes(at:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary of text attributes.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func compositionAttributes(at range: NSRange) -> NSMutableDictionary!
```

```objc
- (NSMutableDictionary *) compositionAttributesAtRange:(NSRange) range;
```

## Return Value

The dictionary of text attributes. The default implementation returns an empty dictionary.

## Parameters

- `range`: The range of text whose attributes you want to obtain.

## See Also

### Working with Ranges
- [func selectionRange() -> NSRange](./selectionrange%28%29.md)
  Returns where the range of the selection that should be placed inside marked text.
- [func replacementRange() -> NSRange](./replacementrange%28%29.md)
  Returns the range in the client document that the text should replace.
- [func mark(forStyle: Int, at: NSRange) -> [AnyHashable : Any]!](./mark%28forstyle,at%29.md)
  Returns a dictionary of text attributes that can mark a range of an attributed string to send to a client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/compositionattributes(at:))*