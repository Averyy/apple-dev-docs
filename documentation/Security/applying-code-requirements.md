# Applying Code Requirements

**Framework**: Security

Manage the code requirements that apply to your signed code.

#### Overview

A code requirement is a condition or constraint that code must satisfy to be considered valid for some purpose. All signed code has implicit or explicit code requirements. Code Signing Services does not have any built-in criteria for why such a constraint is appropriate or useful; it only provides tools for formulating, recording, and evaluating code requirements that you establish. You can specify explicit code requirements when you sign your code, or you can sign the code without specifying any explicit code requirements, in which case the codesign utility typically builds a designated requirement from the name of the program and the chain of signatures securing the code signature. The designated requirement is the set of criteria used to determine whether the signed code is the same code the verifier has seen before.

Code requirements are usually stored in the form of variable-length binary blobs that can be encapsulated as a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) objects. They are retrieved as code requirement objects (objects of type [`SecRequirement`](secrequirement.md)). They can be formulated in a text form that can be compiled into binary form and decompiled back into text form without loss of function (though comments and formatting are not preserved). You can use the functions in the [`Code Signing Services`](code-signing-services.md) API to convert between the various forms of code requirements.

Code requirements and the code signing requirement language are documented in [`Code Signing Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005929).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/applying-code-requirements)*