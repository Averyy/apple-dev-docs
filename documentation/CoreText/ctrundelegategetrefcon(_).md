# CTRunDelegateGetRefCon(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns a run delegate’s “refCon” value.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTRunDelegateGetRefCon(_ runDelegate: CTRunDelegate) -> UnsafeMutableRawPointer
```

```c
extern void *CTRunDelegateGetRefCon(CTRunDelegateRef runDelegate);
```

## Return Value

A constant value associated with the run delegate as an identifier.

## Discussion

The run delegate object was created with the returned “refCon” value.

## Parameters

- `runDelegate`: The run delegate object being queried.

## See Also

### Getting Information About a Run Delegate
- [func CTRunDelegateGetTypeID() -> CFTypeID](./ctrundelegategettypeid%28%29.md)
  Returns the type of CTRunDelegate objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrundelegategetrefcon(_:))*