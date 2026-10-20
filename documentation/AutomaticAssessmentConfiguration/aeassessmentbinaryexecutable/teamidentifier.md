# teamIdentifier

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

Team identifier the running executable’s signature must match, or `nil` to skip the team check.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var teamIdentifier: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * teamIdentifier;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentbinaryexecutable/teamidentifier)*