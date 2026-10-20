# shared

**Framework**: ClassKit  
**Kind**: property  
**Role**: Type Property

The shared data store object.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class var shared: CLSDataStore { get }
```

```objc
@property (class, nonatomic, strong, readonly) CLSDataStore * shared;
```

#### Discussion

When working with the data store, always use this shared instance. Don’t create a new instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsdatastore/shared)*