# Booleans

**Framework**: App Intents  
**Role**: API Collection

Configure the details for parameter variables that contain Boolean values.

## Topics

### Creating an intent parameter
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, displayName: Bool.IntentDisplayName?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](./intentparameter/init%28title,description,default,displayname,requestvaluedialog,inputconnectionbehavior%29.md)
  Creates an app intent parameter.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, displayName: Bool.IntentDisplayName?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./intentparameter/init%28title,description,default,displayname,requestvaluedialog,inputconnectionbehavior,resolvers%29.md)
  Creates an app intent parameter that can convert the selected value.
### Specifying the display name
- [var displayName: Bool.IntentDisplayName?](./intentparameter/displayname.md)

## See Also

### Creating an intent parameter for primitive types
- [Integers](./intentparameter-int.md)
  Configure the details for parameter variables that contain integers.
- [Doubles](./intentparameter-double.md)
  Configure the details for parameter variables that contain floating-point values.
- [Strings](./intentparameter-string.md)
  Configure the details for parameter variables that contain strings or attributed strings.
- [URLs](./intentparameter-url.md)
  Configure the details for parameter variables that contain URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-boolean)*