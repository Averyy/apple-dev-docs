# string

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Allows the client to specify a single string for searching.

**Availability**:
- macOS

## Declaration

```swift
optional var string: String { get }
```

```objc
@property (strong, readonly) NSString * string;
```

## Discussion

If the client cannot logically or efficiently flatten itself into a single string, then the [`string(at:effectiveRange:endsWithSearchBoundary:)`](./string%28at,effectiverange,endswithsearchboundary%29.md) and [`stringLength()`](./stringlength%28%29.md) methods should be implemented instead.

## See Also

### String Searching
- [func string(at: Int, effectiveRange: NSRangePointer, endsWithSearchBoundary: UnsafeMutablePointer<ObjCBool>) -> String](./string%28at,effectiverange,endswithsearchboundary%29.md)
  Returns the found string that is created by conceptually mapping its content to a single string, which is composed of a concatenation of all its substrings.
- [func stringLength() -> Int](./stringlength%28%29.md)
  Returns the full length of the conceptually concatenated string return by the `stringAtIndex:effectiveRange:endsWithSearchBoundary:` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/string)*