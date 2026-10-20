# CFDateGetTypeID()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the type identifier for the `CFDate` opaque type.

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
func CFDateGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CFDateGetTypeID();
```

#### Return Value

The type identifier for the CFDate opaque type.

## See Also

### CFDate Miscellaneous Functions
- [func CFDateCompare(CFDate!, CFDate!, UnsafeMutableRawPointer!) -> CFComparisonResult](./cfdatecompare%28_,_,_%29.md)
  Compares two `CFDate` objects and returns a comparison result.
- [func CFDateCreate(CFAllocator!, CFAbsoluteTime) -> CFDate!](./cfdatecreate%28_,_%29.md)
  Creates a `CFDate` object given an absolute time.
- [func CFDateGetAbsoluteTime(CFDate!) -> CFAbsoluteTime](./cfdategetabsolutetime%28_%29.md)
  Returns a `CFDate` object’s absolute time.
- [func CFDateGetTimeIntervalSinceDate(CFDate!, CFDate!) -> CFTimeInterval](./cfdategettimeintervalsincedate%28_,_%29.md)
  Returns the number of elapsed seconds between the given `CFDate` objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdategettypeid())*