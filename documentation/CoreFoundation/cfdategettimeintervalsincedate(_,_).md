# CFDateGetTimeIntervalSinceDate(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the number of elapsed seconds between the given `CFDate` objects.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFDateGetTimeIntervalSinceDate(_ theDate: CFDate!, _ otherDate: CFDate!) -> CFTimeInterval
```

```c
extern CFTimeInterval CFDateGetTimeIntervalSinceDate(CFDateRef theDate, CFDateRef otherDate);
```

#### Return Value

The number of elapsed seconds between `theDate` and `otherDate`. The result is positive if `theDate` is later than `otherDate`.

## Parameters

- `theDate`: The date to compare to `otherDate`.
- `otherDate`: The date to compare to `theDate`.

## See Also

### CFDate Miscellaneous Functions
- [func CFDateCompare(CFDate!, CFDate!, UnsafeMutableRawPointer!) -> CFComparisonResult](./cfdatecompare%28_,_,_%29.md)
  Compares two `CFDate` objects and returns a comparison result.
- [func CFDateCreate(CFAllocator!, CFAbsoluteTime) -> CFDate!](./cfdatecreate%28_,_%29.md)
  Creates a `CFDate` object given an absolute time.
- [func CFDateGetAbsoluteTime(CFDate!) -> CFAbsoluteTime](./cfdategetabsolutetime%28_%29.md)
  Returns a `CFDate` object’s absolute time.
- [func CFDateGetTypeID() -> CFTypeID](./cfdategettypeid%28%29.md)
  Returns the type identifier for the `CFDate` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdategettimeintervalsincedate(_:_:))*