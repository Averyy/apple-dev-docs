# init(description:default:requestValueDialog:inputConnectionBehavior:resolvers:)

**Framework**: App Intents  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
convenience init<Spec>(description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default, @ResolverSpecificationBuilder<Value.UnwrappedType> resolvers: @escaping () -> Spec) where Spec : ResolverSpecification
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(description:default:requestvaluedialog:inputconnectionbehavior:resolvers:)-4sumo)*