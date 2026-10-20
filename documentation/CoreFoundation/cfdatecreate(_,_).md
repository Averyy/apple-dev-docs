# CFDateCreate(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a `CFDate` object given an absolute time.

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
func CFDateCreate(_ allocator: CFAllocator!, _ at: CFAbsoluteTime) -> CFDate!
```

```c
extern CFDateRefCFDateCreate(CFAllocatorRef allocator, CFAbsoluteTime at);
```

#### Return Value

A date object that represents the absolute time `at`.  The caller is responsible for releasing the `CFDate` object using [`CFRelease`](./cfrelease.md).

#### Discussion

`CFDate` objects must always be created using absolute time. Time intervals are not supported.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `at`: The absolute time to convert to a CFDate object.

## See Also

### CFDate Miscellaneous Functions
- [func CFDateCompare(CFDate!, CFDate!, UnsafeMutableRawPointer!) -> CFComparisonResult](./cfdatecompare%28_,_,_%29.md)
  Compares two `CFDate` objects and returns a comparison result.
- [func CFDateGetAbsoluteTime(CFDate!) -> CFAbsoluteTime](./cfdategetabsolutetime%28_%29.md)
  Returns a `CFDate` object’s absolute time.
- [func CFDateGetTimeIntervalSinceDate(CFDate!, CFDate!) -> CFTimeInterval](./cfdategettimeintervalsincedate%28_,_%29.md)
  Returns the number of elapsed seconds between the given `CFDate` objects.
- [func CFDateGetTypeID() -> CFTypeID](./cfdategettypeid%28%29.md)
  Returns the type identifier for the `CFDate` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatecreate(_:_:))*