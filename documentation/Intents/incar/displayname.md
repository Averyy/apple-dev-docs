# displayName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The electric vehicle’s user-defined display name.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var displayName: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * displayName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * displayName;
```

#### Discussion

The system displays this value when presenting information about the electric vehicle. The user configures the display name in your app.

## See Also

### Identifying the Car
- [var carIdentifier: String](./caridentifier.md)
  The electric vehicle’s unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/displayname)*