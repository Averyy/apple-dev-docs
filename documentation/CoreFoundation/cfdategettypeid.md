# CFDateGetTypeID()

**Framework**: Core Foundation  
**Kind**: func

Returns the type identifier for the `CFDate` opaque type.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFDateGetTypeID() -> CFTypeID
```

#### Return Value

The type identifier for the CFDate opaque type.

## See Also

- [func CFDateCompare(CFDate!, CFDate!, UnsafeMutableRawPointer!) -> CFComparisonResult](cfdatecompare(_:_:_:).md)
  Compares two `CFDate` objects and returns a comparison result.
- [func CFDateCreate(CFAllocator!, CFAbsoluteTime) -> CFDate!](cfdatecreate(_:_:).md)
  Creates a `CFDate` object given an absolute time.
- [func CFDateGetAbsoluteTime(CFDate!) -> CFAbsoluteTime](cfdategetabsolutetime(_:).md)
  Returns a `CFDate` object’s absolute time.
- [func CFDateGetTimeIntervalSinceDate(CFDate!, CFDate!) -> CFTimeInterval](cfdategettimeintervalsincedate(_:_:).md)
  Returns the number of elapsed seconds between the given `CFDate` objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdategettypeid())*