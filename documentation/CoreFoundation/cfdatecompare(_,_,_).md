# CFDateCompare(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Compares two `CFDate` objects and returns a comparison result.

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
func CFDateCompare(_ theDate: CFDate!, _ otherDate: CFDate!, _ context: UnsafeMutableRawPointer!) -> CFComparisonResult
```

```c
extern CFComparisonResult CFDateCompare(CFDateRef theDate, CFDateRef otherDate, void *context);
```

## Return Value

A [`CFComparisonResult`](./cfcomparisonresult.md) value that indicates whether `theDate` is equal to, less than, or greater than `otherDate`.

## Parameters

- `theDate`: The date to compare to `otherDate`.
- `otherDate`: The date to compare to `theDate`.
- `context`: Unused. Pass `NULL`.

## See Also

### CFDate Miscellaneous Functions
- [func CFDateCreate(CFAllocator!, CFAbsoluteTime) -> CFDate!](./cfdatecreate%28_,_%29.md)
  Creates a `CFDate` object given an absolute time.
- [func CFDateGetAbsoluteTime(CFDate!) -> CFAbsoluteTime](./cfdategetabsolutetime%28_%29.md)
  Returns a `CFDate` object’s absolute time.
- [func CFDateGetTimeIntervalSinceDate(CFDate!, CFDate!) -> CFTimeInterval](./cfdategettimeintervalsincedate%28_,_%29.md)
  Returns the number of elapsed seconds between the given `CFDate` objects.
- [func CFDateGetTypeID() -> CFTypeID](./cfdategettypeid%28%29.md)
  Returns the type identifier for the `CFDate` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatecompare(_:_:_:))*