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
template <typename T, typename U, typename P1, typename P2, typename = detail::detail::WhenOrderable<T * *, U * *>> bool operator>=(const bounded_ptr<T, P1> & a, const bounded_ptr<U, P2> & b);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/libkern/operator_=-48u68)*