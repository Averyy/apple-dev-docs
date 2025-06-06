# endSubelementIndex

**Framework**: Foundation  
**Kind**: property

Sets the index position of the last sub-element within the range of objects being tested that pass the specifier’s test.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var endSubelementIndex: Int { get set }
```

#### Discussion

Used only if the end sub-element identifier is `NSIndexSubelement`.

## Parameters

- `index`: The index position of the end sub-element.

## See Also

- [var endSubelementIdentifier: NSWhoseSpecifier.SubelementIdentifier](nswhosespecifier/endsubelementidentifier.md)
  Sets the end sub-element identifier for the specifier to the value of a given sub-element.
- [var startSubelementIdentifier: NSWhoseSpecifier.SubelementIdentifier](nswhosespecifier/startsubelementidentifier.md)
  Returns the start sub-element identifier for the receiver.
- [var startSubelementIndex: Int](nswhosespecifier/startsubelementindex.md)
  Returns the index position of the first sub-element within the range of objects being tested that pass the receiver’s test.
- [var test: NSScriptWhoseTest](nswhosespecifier/test.md)
  Returns the test object encapsulated by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nswhosespecifier/endsubelementindex)*