# ar_data_providers_enumerator_t

**Framework**: ARKit  
**Kind**: typealias

A handler for enumerating a collection of data providers.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
typedef _Bool (^)(NSObject<OS_ar_data_provider> *) ar_data_providers_enumerator_t;
```

## See Also

- [ar_data_provider_state_t](ar_data_provider_state_t.md)
  The possible states of a data provider.
- [ar_data_provider_get_required_authorization_type](ar_data_provider_get_required_authorization_type.md)
  The kinds of authorization you need to use a particular data provider type.
- [ar_data_provider_get_state](ar_data_provider_get_state.md)
  Gets the current status of data coming from this provider.
- [ar_data_providers_t](ar_data_providers_t.md)
  A collection of data providers.
- [ar_data_providers_add_data_provider](ar_data_providers_add_data_provider.md)
  Adds a data provider to a collection.
- [ar_data_providers_add_data_providers](ar_data_providers_add_data_providers.md)
  Adds multiple data providers to a collection.
- [ar_data_providers_create](ar_data_providers_create.md)
  Creates an empty collection of data providers.
- [ar_data_providers_create_with_data_providers](ar_data_providers_create_with_data_providers.md)
  Creates a collection of data providers that contains the data providers you supply.
- [ar_data_providers_enumerate_data_providers_f](ar_data_providers_enumerate_data_providers_f.md)
  Enumerates a collection of data providers.
- [ar_data_providers_get_count](ar_data_providers_get_count.md)
  Gets the number of data providers in a collection.
- [ar_data_providers_enumerate_data_providers](ar_data_providers_enumerate_data_providers.md)
  Enumerates a collection of data providers.
- [ar_data_providers_remove_data_provider](ar_data_providers_remove_data_provider.md)
  Removes a data provider from a collection.
- [ar_data_providers_remove_data_providers](ar_data_providers_remove_data_providers.md)
  Removes multiple data providers from a collection.
- [ar_data_providers_enumerator_function_t](ar_data_providers_enumerator_function_t.md)
- [ar_session_data_provider_state_change_handler_function_t](ar_session_data_provider_state_change_handler_function_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_data_providers_enumerator_t)*