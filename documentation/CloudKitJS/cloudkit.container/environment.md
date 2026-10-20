# environment

**Framework**: CloudKit JS  
**Kind**: property  
**Role**: Instance Property

The container environment, either development or production.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
attribute String environment;
```

#### Discussion

Possible values are [`CloudKit`](../cloudkit.md).[`DEVELOPMENT_ENVIRONMENT`](../cloudkit/development_environment.md)and [`CloudKit`](../cloudkit.md).[`PRODUCTION_ENVIRONMENT`](../cloudkit/production_environment.md).

## See Also

### Getting the Identifier and Environment
- [containerIdentifier](./containeridentifier.md)
  The string that identifies the app’s container.
- [apnsEnvironment](./apnsenvironment.md)
  The Apple Push Notification service (APNs) environment associated with this container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/environment)*