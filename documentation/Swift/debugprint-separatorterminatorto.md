# debugPrint(_:separator:terminator:to:)

**Framework**: Swift  
**Kind**: func

Writes the textual representations of the given items most suitable for debugging into the given output stream.

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
func debugPrint<Target>(_ items: Any..., separator: String = " ", terminator: String = "\n", to output: inout Target) where Target : TextOutputStream
```

#### Discussion

You can pass zero or more items to the `debugPrint(_:separator:terminator:to:)` function. The textual representation for each item is the same as that obtained by calling `String(reflecting: item)`. The following example prints a closed range of integers to a string:

```swift
var range = "My range: "
debugPrint(1...5, to: &range)
// range == "My range: ClosedRange(1...5)\n"
```

To print the items separated by something other than a space, pass a string as `separator`.

```swift
var separated = ""
debugPrint(1.0, 2.0, 3.0, 4.0, 5.0, separator: " ... ", to: &separated)
// separated == "1.0 ... 2.0 ... 3.0 ... 4.0 ... 5.0\n"
```

The output from each call to `debugPrint(_:separator:terminator:to:)` includes a newline by default. To print the items without a trailing newline, pass an empty string as `terminator`.

```swift
var numbers = ""
for n in 1...5 {
    debugPrint(n, terminator: "", to: &numbers)
}
// numbers == "12345"
```

## Parameters

- `items`: Zero or more items to print.
- `separator`: A string to print between each item. The default is a single   space ( ).
- `terminator`: The string to print after all items have been printed. The   default is a newline ( ).
- `output`: An output stream to receive the text representation of each   item.

## See Also

- [func print(Any..., separator: String, terminator: String)](print(_:separator:terminator:).md)
  Writes the textual representations of the given items into the standard output.
- [func print<Target>(Any..., separator: String, terminator: String, to: inout Target)](print(_:separator:terminator:to:).md)
  Writes the textual representations of the given items into the given output stream.
- [func debugPrint(Any..., separator: String, terminator: String)](debugprint(_:separator:terminator:).md)
  Writes the textual representations of the given items most suitable for debugging into the standard output.
- [func dump<T>(T, name: String?, indent: Int, maxDepth: Int, maxItems: Int) -> T](dump(_:name:indent:maxdepth:maxitems:).md)
  Dumps the given object’s contents using its mirror to standard output.
- [func dump<T, TargetStream>(T, to: inout TargetStream, name: String?, indent: Int, maxDepth: Int, maxItems: Int) -> T](dump(_:to:name:indent:maxdepth:maxitems:).md)
  Dumps the given object’s contents using its mirror to the specified output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/debugprint(_:separator:terminator:to:))*