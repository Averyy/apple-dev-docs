# operator==

**Framework**: DriverKit  
**Kind**: func

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
template <typename T, typename P1, typename U, typename P2, typename = detail::detail::WhenComparable<T * *, U * *>> bool operator==(const bounded_ptr<T, P1> & a, const bounded_ptr<U, P2> & b);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/libkern/operator==-96xsq)*