# isValidJSONObject(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether the serializer can convert a given object to JSON data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func isValidJSONObject(_ obj: Any) -> Bool
```

#### Return Value

`true` if `obj` can be converted to JSON data; otherwise, `false`.

## Parameters

- `obj`: The object to test.

## See Also

- [class func data(withJSONObject: Any, options: JSONSerialization.WritingOptions) throws -> Data](jsonserialization/data(withjsonobject:options:).md)
  Returns JSON data from a Foundation object.
- [class func writeJSONObject(Any, to: OutputStream, options: JSONSerialization.WritingOptions, error: NSErrorPointer) -> Int](jsonserialization/writejsonobject(_:to:options:error:).md)
  Writes a given JSON object to a stream.
- [JSONSerialization.WritingOptions](jsonserialization/writingoptions.md)
  Options for writing JSON data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/isvalidjsonobject(_:))*