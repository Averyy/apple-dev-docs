# operator>

**Framework**: DriverKit  
**Kind**: func

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
template <typename T, typename U, typename P, typename = detail::detail::WhenOrderable<T * *, U * *>> bool operator>(T * * a, const bounded_ptr<U, P> & b);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/libkern/operator_-1teoa)*