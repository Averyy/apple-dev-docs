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
template <typename T, typename P, typename U, typename = detail::detail::WhenComparable<T * *, U * *>> bool operator==(U * * a, const bounded_ptr<T, P> & b);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/libkern/operator==-15jrb)*