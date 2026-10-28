# configurationsByBinaryExecutable

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

The collection of executable participants available during an assessment, along with their associated configurations.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var configurationsByBinaryExecutable: [AEAssessmentBinaryExecutable : AEAssessmentBinaryExecutableConfiguration] { get }
```

```objc
@property (nonatomic, copy, readonly) NSDictionary<AEAssessmentBinaryExecutable *,AEAssessmentBinaryExecutableConfiguration *> * configurationsByBinaryExecutable;
```

## Discussion

Add executables with [`setConfiguration(_:for:)`](./setconfiguration%28_,for%29-16sed.md) and remove them with `AEAssessmentConfiguration/removeBinaryExecutable(_:)`.

> **See Also**: [`AEAssessmentBinaryExecutable`](../aeassessmentbinaryexecutable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/configurationsbybinaryexecutable)*