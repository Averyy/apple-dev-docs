# fetchRequestFromTemplate(withName:substitutionVariables:)

**Framework**: Core Data  
**Kind**: method

Returns a copy of the fetch request template with the variables substituted by values from the substitutions dictionary.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func fetchRequestFromTemplate(withName name: String, substitutionVariables variables: [String : Any]) -> NSFetchRequest<any NSFetchRequestResult>?
```

#### Return Value

A copy of the fetch request template with the variables substituted by values from `variables`.

#### Discussion

The `variables` dictionary must provide values for all the variables. If you want to test for a nil value, use `[NSNull null]`.

This method provides the usual way to bind an “abstractly” defined fetch request template to a concrete fetch. For more details on using this method, see [`Creating Predicates`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pCreating.html#//apple_ref/doc/uid/TP40001793).

## Parameters

- `name`: A string containing the name of a fetch request template.
- `variables`: A dictionary containing key-value pairs where the keys are the names of variables specified in the template; the corresponding values are substituted before the fetch request is returned. The dictionary must provide values for all the variables in the template.

## See Also

- [var fetchRequestTemplatesByName: [String : NSFetchRequest<any NSFetchRequestResult>]](nsmanagedobjectmodel/fetchrequesttemplatesbyname.md)
  A dictionary of the receiver’s fetch request templates, keyed by name.
- [func fetchRequestTemplate(forName: String) -> NSFetchRequest<any NSFetchRequestResult>?](nsmanagedobjectmodel/fetchrequesttemplate(forname:).md)
  Returns the fetch request with a specified name.
- [func setFetchRequestTemplate(NSFetchRequest<any NSFetchRequestResult>?, forName: String)](nsmanagedobjectmodel/setfetchrequesttemplate(_:forname:).md)
  Associates the specified fetch request with the receiver using the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/fetchrequestfromtemplate(withname:substitutionvariables:))*