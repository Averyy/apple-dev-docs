# setFetchRequestTemplate(_:forName:)

**Framework**: Core Data  
**Kind**: method

Associates the specified fetch request with the receiver using the given name.

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
func setFetchRequestTemplate(_ fetchRequestTemplate: NSFetchRequest<any NSFetchRequestResult>?, forName name: String)
```

#### Discussion

For more details on using this method, see [`Creating Predicates`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pCreating.html#//apple_ref/doc/uid/TP40001793).

##### Special Considerations

This method raises an exception if the receiver has been used by an object graph manager.

## Parameters

- `fetchRequestTemplate`: A fetch request, typically containing predicates with variables for substitution.
- `name`: A string that specifies the name of the fetch request template.

## See Also

- [var fetchRequestTemplatesByName: [String : NSFetchRequest<any NSFetchRequestResult>]](nsmanagedobjectmodel/fetchrequesttemplatesbyname.md)
  A dictionary of the receiver’s fetch request templates, keyed by name.
- [func fetchRequestTemplate(forName: String) -> NSFetchRequest<any NSFetchRequestResult>?](nsmanagedobjectmodel/fetchrequesttemplate(forname:).md)
  Returns the fetch request with a specified name.
- [func fetchRequestFromTemplate(withName: String, substitutionVariables: [String : Any]) -> NSFetchRequest<any NSFetchRequestResult>?](nsmanagedobjectmodel/fetchrequestfromtemplate(withname:substitutionvariables:).md)
  Returns a copy of the fetch request template with the variables substituted by values from the substitutions dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/setfetchrequesttemplate(_:forname:))*