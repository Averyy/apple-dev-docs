# unlock()

**Framework**: Core Animation  
**Kind**: method  
**Role**: Type Method

Relinquishes a previously acquired transaction lock.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func unlock()
```

```objc
+ (void) unlock;
```

## See Also

### Managing Concurrency
- [class func lock()](./lock%28%29.md)
  Attempts to acquire a recursive spin-lock lock, ensuring that returned layer values are valid until unlocked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/unlock())*