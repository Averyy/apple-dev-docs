# startSubelementIndex

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the index position of the first sub-element within the range of objects being tested that pass the receiver’s test.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var startSubelementIndex: Int { get set }
```

```objc
@property NSInteger startSubelementIndex;
```

## Return Value

The index position of the first sub-element within the range of objects being tested that pass the receiver’s test.

## See Also

### Accessing information about a whose specifier
- [var endSubelementIdentifier: NSWhoseSpecifier.SubelementIdentifier](./endsubelementidentifier.md)
  Sets the end sub-element identifier for the specifier to the value of a given sub-element.
- [var endSubelementIndex: Int](./endsubelementindex.md)
  Sets the index position of the last sub-element within the range of objects being tested that pass the specifier’s test.
- [var startSubelementIdentifier: NSWhoseSpecifier.SubelementIdentifier](./startsubelementidentifier.md)
  Returns the start sub-element identifier for the receiver.
- [var test: NSScriptWhoseTest](./test.md)
  Returns the test object encapsulated by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nswhosespecifier/startsubelementindex)*