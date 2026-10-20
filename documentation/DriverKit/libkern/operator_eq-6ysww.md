# operator>=

**Framework**: DriverKit  
**Kind**: func  
**Role**: Function Template

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
template <typename T, typename U, typename P, typename = detail::detail::WhenOrderable<T * *, U * *>> bool operator>=(T * *a, const bounded_ptr<U, P> & b);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/libkern/operator_=-6ysww)*