# dump(_:name:indent:maxDepth:maxItems:)

**Framework**: Swift  
**Kind**: func

Dumps the given object’s contents using its mirror to standard output.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@discardableResult
func dump<T>(_ value: T, name: String? = nil, indent: Int = 0, maxDepth: Int = .max, maxItems: Int = .max) -> T
```

#### Return Value

The instance passed as `value`.

## Parameters

- `value`: The value to output to the   stream.
- `name`: A label to use when writing the contents of  . When    is passed, the label is omitted. The default is  .
- `indent`: The number of spaces to use as an indent for each line of the   output. The default is  .
- `maxDepth`: The maximum depth to descend when writing the contents of a   value that has nested components. The default is  .
- `maxItems`: The maximum number of elements for which to write the full   contents. The default is  .

## See Also

- [func print(Any..., separator: String, terminator: String)](print(_:separator:terminator:).md)
  Writes the textual representations of the given items into the standard output.
- [func print<Target>(Any..., separator: String, terminator: String, to: inout Target)](print(_:separator:terminator:to:).md)
  Writes the textual representations of the given items into the given output stream.
- [func debugPrint(Any..., separator: String, terminator: String)](debugprint(_:separator:terminator:).md)
  Writes the textual representations of the given items most suitable for debugging into the standard output.
- [func debugPrint<Target>(Any..., separator: String, terminator: String, to: inout Target)](debugprint(_:separator:terminator:to:).md)
  Writes the textual representations of the given items most suitable for debugging into the given output stream.
- [func dump<T, TargetStream>(T, to: inout TargetStream, name: String?, indent: Int, maxDepth: Int, maxItems: Int) -> T](dump(_:to:name:indent:maxdepth:maxitems:).md)
  Dumps the given object’s contents using its mirror to the specified output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dump(_:name:indent:maxdepth:maxitems:))*