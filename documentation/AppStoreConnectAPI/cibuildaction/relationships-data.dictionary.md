# CiBuildAction.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships of the Build Actions resource you included in the request and those on which you can operate.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiBuildAction.Relationships
```

## Topics

### Objects
- [object CiBuildAction.Relationships.BuildRun](./relationships-data.dictionary/buildrun-data.dictionary.md)
  The data and links that describe the relationship between the Build Actions and Build Runs resources.
### Dictionaries
- [object CiBuildAction.Relationships.Artifacts](./relationships-data.dictionary/artifacts-data.dictionary.md)
- [object CiBuildAction.Relationships.Issues](./relationships-data.dictionary/issues-data.dictionary.md)
- [object CiBuildAction.Relationships.TestResults](./relationships-data.dictionary/testresults-data.dictionary.md)

## Properties

- `artifacts` (CiBuildAction.Relationships.Artifacts)
- `buildRun` (CiBuildAction.Relationships.BuildRun): The data and links that describe the relationship between the Build Actions and the Build Runs resources.
- `issues` (CiBuildAction.Relationships.Issues)
- `testResults` (CiBuildAction.Relationships.TestResults)

## See Also

### Objects
- [object CiBuildAction.Attributes](./attributes-data.dictionary.md)
  The attributes that describe a Build Actions resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildaction/relationships-data.dictionary)*