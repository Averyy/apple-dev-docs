# endSubelementIdentifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the end sub-element identifier for the specifier to the value of a given sub-element.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var endSubelementIdentifier: NSWhoseSpecifier.SubelementIdentifier { get set }
```

```objc
@property NSWhoseSubelementIdentifier endSubelementIdentifier;
```

## Parameters

- `subelement`: The end sub-element for the receiver.

## See Also

### Accessing information about a whose specifier
- [var endSubelementIndex: Int](./endsubelementindex.md)
  Sets the index position of the last sub-element within the range of objects being tested that pass the specifier’s test.
- [var startSubelementIdentifier: NSWhoseSpecifier.SubelementIdentifier](./startsubelementidentifier.md)
  Returns the start sub-element identifier for the receiver.
- [var startSubelementIndex: Int](./startsubelementindex.md)
  Returns the index position of the first sub-element within the range of objects being tested that pass the receiver’s test.
- [var test: NSScriptWhoseTest](./test.md)
  Returns the test object encapsulated by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nswhosespecifier/endsubelementidentifier)*