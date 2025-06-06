# CFDateCreate(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a `CFDate` object given an absolute time.

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
func CFDateCreate(_ allocator: CFAllocator!, _ at: CFAbsoluteTime) -> CFDate!
```

#### Return Value

A date object that represents the absolute time `at`.  The caller is responsible for releasing the `CFDate` object using [`CFRelease`](cfrelease.md).

#### Discussion

`CFDate` objects must always be created using absolute time. Time intervals are not supported.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `at`: The absolute time to convert to a CFDate object.

## See Also

- [func CFDateCompare(CFDate!, CFDate!, UnsafeMutableRawPointer!) -> CFComparisonResult](cfdatecompare(_:_:_:).md)
  Compares two `CFDate` objects and returns a comparison result.
- [func CFDateGetAbsoluteTime(CFDate!) -> CFAbsoluteTime](cfdategetabsolutetime(_:).md)
  Returns a `CFDate` object’s absolute time.
- [func CFDateGetTimeIntervalSinceDate(CFDate!, CFDate!) -> CFTimeInterval](cfdategettimeintervalsincedate(_:_:).md)
  Returns the number of elapsed seconds between the given `CFDate` objects.
- [func CFDateGetTypeID() -> CFTypeID](cfdategettypeid().md)
  Returns the type identifier for the `CFDate` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatecreate(_:_:))*