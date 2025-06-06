# Objective-C Runtime

**Framework**: Objective-C Runtime

Describes the macOS Objective-C runtime library support functions and data structures.

#### Overview

The Objective-C runtime is a runtime library that provides support for the dynamic properties of the Objective-C language, and as such is linked to by all Objective-C apps. Objective-C runtime library support functions are implemented in the shared library found at `/usr/lib/libobjc.A.dylib`.

You typically don’t need to use the Objective-C runtime library directly when programming in Objective-C. This API is useful primarily for developing bridge layers between Objective-C and other languages, or for low-level debugging.

The macOS implementation of the Objective-C runtime library is unique to the Mac. For other platforms, the GNU Compiler Collection provides a different implementation with a similar API. This document covers only the macOS implementation.

The low-level Objective-C runtime API is significantly updated in OS X version 10.5. Many functions and all existing data structures are replaced with new functions. The old functions and structures are deprecated in 32-bit and absent in 64-bit mode. The API constrains several values to 32-bit ints even in 64-bit mode—class count, protocol count, methods per class, ivars per class, arguments per method, sizeof(all arguments) per method, and class version number. In addition, the new Objective-C ABI (not described here) further constrains `sizeof(anInstance)` to 32 bits, and three other values to 24 bits—methods per class, ivars per class, and sizeof(a single ivar). Finally, the obsolete `NXHashTable` and `NXMapTable` are limited to 4 billion items.

> **Note**:  All `char *` in the runtime API should be considered to have UTF-8 encoding.

 All `char *` in the runtime API should be considered to have UTF-8 encoding.

“Deprecated” below means “deprecated in OS X version 10.5 for 32-bit code, and disallowed for 64-bit code.”

##### Who Should Read This Document

The document is intended for readers who might be interested in learning about the Objective-C runtime.

Because this isn’t a document about C, it assumes some prior acquaintance with that language. However, it doesn’t have to be an extensive acquaintance.

## Topics

### Working with Classes
- [func class_getName(AnyClass?) -> UnsafePointer<CChar>](class_getname(_:).md)
  Returns the name of a class.
- [func class_getSuperclass(AnyClass?) -> AnyClass?](class_getsuperclass(_:).md)
  Returns the superclass of a class.
- [func class_setSuperclass(AnyClass, AnyClass) -> AnyClass](class_setsuperclass(_:_:).md)
  Sets the superclass of a given class.
- [func class_isMetaClass(AnyClass?) -> Bool](class_ismetaclass(_:).md)
  Returns a Boolean value that indicates whether a class object is a metaclass.
- [func class_getInstanceSize(AnyClass?) -> Int](class_getinstancesize(_:).md)
  Returns the size of instances of a class.
- [func class_getInstanceVariable(AnyClass?, UnsafePointer<CChar>) -> Ivar?](class_getinstancevariable(_:_:).md)
  Returns the `Ivar` for a specified instance variable of a given class.
- [func class_getClassVariable(AnyClass?, UnsafePointer<CChar>) -> Ivar?](class_getclassvariable(_:_:).md)
  Returns the `Ivar` for a specified class variable of a given class.
- [func class_addIvar(AnyClass?, UnsafePointer<CChar>, Int, UInt8, UnsafePointer<CChar>?) -> Bool](class_addivar(_:_:_:_:_:).md)
  Adds a new instance variable to a class.
- [func class_copyIvarList(AnyClass?, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<Ivar>?](class_copyivarlist(_:_:).md)
  Describes the instance variables declared by a class.
- [func class_getIvarLayout(AnyClass?) -> UnsafePointer<UInt8>?](class_getivarlayout(_:).md)
  Returns a description of the `Ivar` layout for a given class.
- [func class_setIvarLayout(AnyClass?, UnsafePointer<UInt8>?)](class_setivarlayout(_:_:).md)
  Sets the `Ivar` layout for a given class.
- [func class_getWeakIvarLayout(AnyClass?) -> UnsafePointer<UInt8>?](class_getweakivarlayout(_:).md)
  Returns a description of the layout of weak `Ivar`s for a given class.
- [func class_setWeakIvarLayout(AnyClass?, UnsafePointer<UInt8>?)](class_setweakivarlayout(_:_:).md)
  Sets the layout for weak `Ivar`s for a given class.
- [func class_getProperty(AnyClass?, UnsafePointer<CChar>) -> objc_property_t?](class_getproperty(_:_:).md)
  Returns a property with a given name of a given class.
- [func class_copyPropertyList(AnyClass?, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_t>?](class_copypropertylist(_:_:).md)
  Describes the properties declared by a class.
- [func class_addMethod(AnyClass?, Selector, IMP, UnsafePointer<CChar>?) -> Bool](class_addmethod(_:_:_:_:).md)
  Adds a new method to a class with a given name and implementation.
- [func class_getInstanceMethod(AnyClass?, Selector) -> Method?](class_getinstancemethod(_:_:).md)
  Returns a specified instance method for a given class.
- [func class_getClassMethod(AnyClass?, Selector) -> Method?](class_getclassmethod(_:_:).md)
  Returns a pointer to the data structure describing a given class method for a given class.
- [func class_copyMethodList(AnyClass?, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<Method>?](class_copymethodlist(_:_:).md)
  Describes the instance methods implemented by a class.
- [func class_replaceMethod(AnyClass?, Selector, IMP, UnsafePointer<CChar>?) -> IMP?](class_replacemethod(_:_:_:_:).md)
  Replaces the implementation of a method for a given class.
- [func class_getMethodImplementation(AnyClass?, Selector) -> IMP?](class_getmethodimplementation(_:_:).md)
  Returns the function pointer that would be called if a particular message were sent to an instance of a class.
- [func class_getMethodImplementation_stret(AnyClass?, Selector) -> IMP?](class_getmethodimplementation_stret(_:_:).md)
  Returns the function pointer that would be called if a particular message were sent to an instance of a class.
- [func class_respondsToSelector(AnyClass?, Selector) -> Bool](class_respondstoselector(_:_:).md)
  Returns a Boolean value that indicates whether instances of a class respond to a particular selector.
- [func class_addProtocol(AnyClass?, Protocol) -> Bool](class_addprotocol(_:_:).md)
  Adds a protocol to a class.
- [func class_addProperty(AnyClass?, UnsafePointer<CChar>, UnsafePointer<objc_property_attribute_t>?, UInt32) -> Bool](class_addproperty(_:_:_:_:).md)
  Adds a property to a class.
- [func class_replaceProperty(AnyClass?, UnsafePointer<CChar>, UnsafePointer<objc_property_attribute_t>?, UInt32)](class_replaceproperty(_:_:_:_:).md)
  Replace a property of a class.
- [func class_conformsToProtocol(AnyClass?, Protocol?) -> Bool](class_conformstoprotocol(_:_:).md)
  Returns a Boolean value that indicates whether a class conforms to a given protocol.
- [func class_copyProtocolList(AnyClass?, UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<Protocol>?](class_copyprotocollist(_:_:).md)
  Describes the protocols adopted by a class.
- [func class_getVersion(AnyClass?) -> Int32](class_getversion(_:).md)
  Returns the version number of a class definition.
- [func class_setVersion(AnyClass?, Int32)](class_setversion(_:_:).md)
  Sets the version number of a class definition.
- [objc_setFutureClass](1808430-objc_setfutureclass.md)
  Used by CoreFoundation’s toll-free bridging.
### Adding Classes
- [func objc_allocateClassPair(AnyClass?, UnsafePointer<CChar>, Int) -> AnyClass?](objc_allocateclasspair(_:_:_:).md)
  Creates a new class and metaclass.
- [func objc_disposeClassPair(AnyClass)](objc_disposeclasspair(_:).md)
  Destroys a class and its associated metaclass.
- [func objc_registerClassPair(AnyClass)](objc_registerclasspair(_:).md)
  Registers a class that was allocated using [`objc_allocateClassPair(_:_:_:)`](objc_allocateclasspair(_:_:_:).md).
- [func objc_duplicateClass(AnyClass, UnsafePointer<CChar>, Int) -> AnyClass](objc_duplicateclass(_:_:_:).md)
  Used by Foundation’s Key-Value Observing.
### Instantiating Classes
- [func class_createInstance(AnyClass?, Int) -> Any?](class_createinstance(_:_:).md)
  Creates an instance of a class, allocating memory for the class in the default malloc memory zone.
### Working with Instances
- [func object_getIndexedIvars(Any?) -> UnsafeMutableRawPointer?](object_getindexedivars(_:).md)
  Returns a pointer to any extra bytes allocated with a instance given object.
- [func object_getIvar(Any?, Ivar) -> Any?](object_getivar(_:_:).md)
  Reads the value of an instance variable in an object.
- [func object_setIvar(Any?, Ivar, Any?)](object_setivar(_:_:_:).md)
  Sets the value of an instance variable in an object.
- [func object_getClassName(Any?) -> UnsafePointer<CChar>](object_getclassname(_:).md)
  Returns the class name of a given object.
- [func object_getClass(Any?) -> AnyClass?](object_getclass(_:).md)
  Returns the class of an object.
- [func object_setClass(Any?, AnyClass) -> AnyClass?](object_setclass(_:_:).md)
  Sets the class of an object.
### Obtaining Class Definitions
- [func objc_getClassList(AutoreleasingUnsafeMutablePointer<AnyClass>?, Int32) -> Int32](objc_getclasslist(_:_:).md)
  Obtains the list of registered class definitions.
- [func objc_copyClassList(UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<AnyClass>?](objc_copyclasslist(_:).md)
  Creates and returns a list of pointers to all registered class definitions.
- [func objc_lookUpClass(UnsafePointer<CChar>) -> AnyClass?](objc_lookupclass(_:).md)
  Returns the class definition of a specified class.
- [func objc_getClass(UnsafePointer<CChar>) -> Any!](objc_getclass(_:).md)
  Returns the class definition of a specified class.
- [func objc_getRequiredClass(UnsafePointer<CChar>) -> AnyClass](objc_getrequiredclass(_:).md)
  Returns the class definition of a specified class.
- [func objc_getMetaClass(UnsafePointer<CChar>) -> Any!](objc_getmetaclass(_:).md)
  Returns the metaclass definition of a specified class.
### Working with Instance Variables
- [func ivar_getName(Ivar) -> UnsafePointer<CChar>?](ivar_getname(_:).md)
  Returns the name of an instance variable.
- [func ivar_getTypeEncoding(Ivar) -> UnsafePointer<CChar>?](ivar_gettypeencoding(_:).md)
  Returns the type string of an instance variable.
- [func ivar_getOffset(Ivar) -> Int](ivar_getoffset(_:).md)
  Returns the offset of an instance variable.
### Associative References
- [func objc_setAssociatedObject(Any, UnsafeRawPointer, Any?, objc_AssociationPolicy)](objc_setassociatedobject(_:_:_:_:).md)
  Sets an associated value for a given object using a given key and association policy.
- [func objc_getAssociatedObject(Any, UnsafeRawPointer) -> Any?](objc_getassociatedobject(_:_:).md)
  Returns the value associated with a given object for a given key.
- [func objc_removeAssociatedObjects(Any)](objc_removeassociatedobjects(_:).md)
  Removes all associations for a given object.
### Working with Methods
- [func method_getName(Method) -> Selector](method_getname(_:).md)
  Returns the name of a method.
- [func method_getImplementation(Method) -> IMP](method_getimplementation(_:).md)
  Returns the implementation of a method.
- [func method_getTypeEncoding(Method) -> UnsafePointer<CChar>?](method_gettypeencoding(_:).md)
  Returns a string describing a method’s parameter and return types.
- [func method_copyReturnType(Method) -> UnsafeMutablePointer<CChar>](method_copyreturntype(_:).md)
  Returns a string describing a method’s return type.
- [func method_copyArgumentType(Method, UInt32) -> UnsafeMutablePointer<CChar>?](method_copyargumenttype(_:_:).md)
  Returns a string describing a single parameter type of a method.
- [func method_getReturnType(Method, UnsafeMutablePointer<CChar>, Int)](method_getreturntype(_:_:_:).md)
  Returns by reference a string describing a method’s return type.
- [func method_getNumberOfArguments(Method) -> UInt32](method_getnumberofarguments(_:).md)
  Returns the number of arguments accepted by a method.
- [func method_getArgumentType(Method, UInt32, UnsafeMutablePointer<CChar>?, Int)](method_getargumenttype(_:_:_:_:).md)
  Returns by reference a string describing a single parameter type of a method.
- [func method_getDescription(Method) -> UnsafeMutablePointer<objc_method_description>](method_getdescription(_:).md)
  Returns a method description structure for a specified method.
- [func method_setImplementation(Method, IMP) -> IMP](method_setimplementation(_:_:).md)
  Sets the implementation of a method.
- [func method_exchangeImplementations(Method, Method)](method_exchangeimplementations(_:_:).md)
  Exchanges the implementations of two methods.
### Working with Libraries
- [func objc_copyImageNames(UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<CChar>>](objc_copyimagenames(_:).md)
  Returns the names of all the loaded Objective-C frameworks and dynamic libraries.
- [func class_getImageName(AnyClass?) -> UnsafePointer<CChar>?](class_getimagename(_:).md)
  Returns the name of the dynamic library a class originated from.
- [func objc_copyClassNamesForImage(UnsafePointer<CChar>, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<CChar>>?](objc_copyclassnamesforimage(_:_:).md)
  Returns the names of all the classes within a specified library or framework.
### Working with Selectors
- [func sel_getName(Selector) -> UnsafePointer<CChar>](sel_getname(_:).md)
  Returns the name of the method specified by a given selector.
- [func sel_registerName(UnsafePointer<CChar>) -> Selector](sel_registername(_:).md)
  Registers a method with the Objective-C runtime system, maps the method name to a selector, and returns the selector value.
- [func sel_getUid(UnsafePointer<CChar>) -> Selector](sel_getuid(_:).md)
  Registers a method name with the Objective-C runtime system.
- [func sel_isEqual(Selector, Selector) -> Bool](sel_isequal(_:_:).md)
  Returns a Boolean value that indicates whether two selectors are equal.
### Working with Protocols
- [func objc_getProtocol(UnsafePointer<CChar>) -> Protocol?](objc_getprotocol(_:).md)
  Returns a specified protocol.
- [func objc_copyProtocolList(UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<Protocol>?](objc_copyprotocollist(_:).md)
  Returns an array of all the protocols known to the runtime.
- [func objc_allocateProtocol(UnsafePointer<CChar>) -> Protocol?](objc_allocateprotocol(_:).md)
  Creates a new protocol instance.
- [func objc_registerProtocol(Protocol)](objc_registerprotocol(_:).md)
  Registers a newly created protocol with the Objective-C runtime.
- [func protocol_addMethodDescription(Protocol, Selector, UnsafePointer<CChar>?, Bool, Bool)](protocol_addmethoddescription(_:_:_:_:_:).md)
  Adds a method to a protocol.
- [func protocol_addProtocol(Protocol, Protocol)](protocol_addprotocol(_:_:).md)
  Adds a registered protocol to another protocol that is under construction.
- [func protocol_addProperty(Protocol, UnsafePointer<CChar>, UnsafePointer<objc_property_attribute_t>?, UInt32, Bool, Bool)](protocol_addproperty(_:_:_:_:_:_:).md)
  Adds a property to a protocol that is under construction.
- [func protocol_getName(Protocol) -> UnsafePointer<CChar>](protocol_getname(_:).md)
  Returns the name of a protocol.
- [func protocol_isEqual(Protocol?, Protocol?) -> Bool](protocol_isequal(_:_:).md)
  Returns a Boolean value that indicates whether two protocols are equal.
- [func protocol_copyMethodDescriptionList(Protocol, Bool, Bool, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_method_description>?](protocol_copymethoddescriptionlist(_:_:_:_:).md)
  Returns an array of method descriptions of methods meeting a given specification for a given protocol.
- [func protocol_getMethodDescription(Protocol, Selector, Bool, Bool) -> objc_method_description](protocol_getmethoddescription(_:_:_:_:).md)
  Returns a method description structure for a specified method of a given protocol.
- [func protocol_copyPropertyList(Protocol, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_t>?](protocol_copypropertylist(_:_:).md)
  Returns an array of the properties declared by a protocol.
- [func protocol_getProperty(Protocol, UnsafePointer<CChar>, Bool, Bool) -> objc_property_t?](protocol_getproperty(_:_:_:_:).md)
  Returns the specified property of a given protocol.
- [func protocol_copyProtocolList(Protocol, UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<Protocol>?](protocol_copyprotocollist(_:_:).md)
  Returns an array of the protocols adopted by a protocol.
- [func protocol_conformsToProtocol(Protocol?, Protocol?) -> Bool](protocol_conformstoprotocol(_:_:).md)
  Returns a Boolean value that indicates whether one protocol conforms to another protocol.
### Working with Properties
- [func property_getName(objc_property_t) -> UnsafePointer<CChar>](property_getname(_:).md)
  Returns the name of a property.
- [func property_getAttributes(objc_property_t) -> UnsafePointer<CChar>?](property_getattributes(_:).md)
  Returns the attribute string of a property.
- [func property_copyAttributeValue(objc_property_t, UnsafePointer<CChar>) -> UnsafeMutablePointer<CChar>?](property_copyattributevalue(_:_:).md)
  Returns the value of a property attribute given the attribute name.
- [func property_copyAttributeList(objc_property_t, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_attribute_t>?](property_copyattributelist(_:_:).md)
  Returns an array of property attributes for a given property.
### Using Objective-C Language Features
- [func objc_enumerationMutation(Any)](objc_enumerationmutation(_:).md)
  Inserted by the compiler when a mutation is detected during a foreach iteration.
- [func objc_setEnumerationMutationHandler(((Any) -> Void)?)](objc_setenumerationmutationhandler(_:).md)
  Sets the current mutation handler.
- [func imp_implementationWithBlock(Any) -> IMP](imp_implementationwithblock(_:).md)
  Creates a pointer to a function that calls the specified block when the method is called.
- [func imp_getBlock(IMP) -> Any?](imp_getblock(_:).md)
  Returns the block associated with an `IMP` that was created using [`imp_implementationWithBlock(_:)`](imp_implementationwithblock(_:).md).
- [func imp_removeBlock(IMP) -> Bool](imp_removeblock(_:).md)
  Disassociates a block from an `IMP` that was created using [`imp_implementationWithBlock(_:)`](imp_implementationwithblock(_:).md), and releases the copy of the block that was created.
- [func objc_loadWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>) -> Any?](objc_loadweak(_:).md)
  Loads the object referenced by a weak pointer and returns it.
- [func objc_storeWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>, Any?) -> Any?](objc_storeweak(_:_:).md)
  Stores a new value in a `__weak` variable.
### Class-Definition Data Structures
- [typealias Method](method.md)
  An opaque type that represents a method in a class definition.
- [typealias Ivar](ivar.md)
  An opaque type that represents an instance variable.
- [typealias Category](category.md)
  An opaque type that represents a category.
- [typealias objc_property_t](objc_property_t.md)
  An opaque type that represents an Objective-C declared property.
- [typealias IMP](imp.md)
  A pointer to the start of a method implementation.
- [struct objc_method_description](objc_method_description.md)
  Defines an Objective-C method.
- [objc_cache](objc_cache.md)
  Performance optimization for method calls. Contains pointers to recently used methods.
- [struct objc_property_attribute_t](objc_property_attribute_t.md)
  Defines a property attribute.
### Instance Data Types
- [struct objc_object](objc_object.md)
  Represents an instance of a class.
- [struct objc_super](objc_super-swift.struct.md)
  Specifies the superclass of an instance.
### Associative References
- [enum objc_AssociationPolicy](objc_associationpolicy.md)
  Type to specify the behavior of an association.

## See Also

- [Objective-C Runtime Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048)
- [Objective-C Structures](objective-c-structures.md)
- [Objective-C Constants](objective-c-constants.md)
- [Objective-C Functions](objective-c-functions.md)
- [Objective-C Data Types](objective-c-data-types.md)
- [Objective-C Macros](objective-c-macros.md)
- [Objective-C Enumerations](objective-c-enums.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objective-c-runtime)*