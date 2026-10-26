# AEAssessmentConfiguration.AutocorrectMode

**Framework**: Automatic Assessment Configuration  
**Kind**: struct  
**Role**: Structure

The set of autocorrect features that you can enable during an assessment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct AutocorrectMode
```

```c
enum AEAutocorrectMode : NSUInteger;
```

#### Overview

Use one or more of the autocorrect modes to set the [`autocorrectMode`](./autocorrectmode-swift.property.md) property of an [`AEAssessmentConfiguration`](../aeassessmentconfiguration.md) instance. For example, you can enable both spelling and punctuation corrections by combining [`spelling`](./autocorrectmode-swift.struct/spelling.md) and [`punctuation`](./autocorrectmode-swift.struct/punctuation.md):

**Swift**:

```swift
let config = AEAssessmentConfiguration()

#if os(iOS) // Available only on iOS and iPadOS.
config.autocorrectMode = [.punctuation, .spelling]
#endif

let session = AEAssessmentSession(configuration: config)
```

**Objective-C**:

```objc
AEAssessmentConfiguration *config = [AEAssessmentConfiguration new];

#if TARGET_OS_IPHONE || TARGET_IPHONE_SIMULATOR // Available only on iOS and iPadOS.
config.autocorrectMode = AEAutocorrectModePunctuation | AEAutocorrectModeSpelling;
#endif

AEAssessmentSession *session = [[AEAssessmentSession alloc] initWithConfiguration:config];
```

## Topics

### Creating a mode
- [init(rawValue: UInt)](./autocorrectmode-swift.struct/init%28rawvalue%29.md)
  Creates a new mode instance.
### Modes
- [static var punctuation: AEAssessmentConfiguration.AutocorrectMode](./autocorrectmode-swift.struct/punctuation.md)
  A mode in which autocorrect checks punctuation as the user types.
- [static var spelling: AEAssessmentConfiguration.AutocorrectMode](./autocorrectmode-swift.struct/spelling.md)
  A mode in which autocorrect checks for spelling as the user types.
- [AEAutocorrectModeNone](../aeautocorrectmode/aeautocorrectmodenone.md)
  A mode that indicates autocorrect doesn’t check anything.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Allowing corrections
- [var allowsSpellCheck: Bool](./allowsspellcheck.md)
  A Boolean value that indicates whether to allow spell check during an assessment.
- [var autocorrectMode: AEAssessmentConfiguration.AutocorrectMode](./autocorrectmode-swift.property.md)
  A Boolean value that indicates whether to allow Autocorrect during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/autocorrectmode-swift.struct)*