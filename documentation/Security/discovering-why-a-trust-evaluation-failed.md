# Discovering Why a Trust Evaluation Failed

**Framework**: Security

Determine whether you can recover from a failed trust evaluation.

#### Overview

Many factors affect the outcome of a trust evaluation. These include whether the system can locate all of the intermediate certificates, the validity of the certificates in the chain, and the characteristics of the certificates. Some issues, like a revoked certificate, result in an absolute failure and should  be circumvented. In other cases, you might get a different result by changing the conditions of the evaluation. For example, an expired certificate might have been valid when the corresponding identity was used to sign a document.

To get the specific reason for trust failure, examine the error parameter provided in the evaluation callback described in [`Evaluating a Trust and Parsing the Result`](evaluating-a-trust-and-parsing-the-result.md). The error’s code indicates the reason, or in the case of multiple errors, the most serious reason for the failure. For example, a revoked certificate results in an error with the code [`errSecCertificateRevoked`](errseccertificaterevoked.md), while an expired certificate produces [`errSecCertificateExpired`](errseccertificateexpired.md).

To determine whether the system considers the failure recoverable, use the [`SecTrustGetTrustResult(_:_:)`](sectrustgettrustresult(_:_:).md) method.

For a result of [`SecTrustResultType.recoverableTrustFailure`](sectrustresulttype/recoverabletrustfailure.md), and based on the error you receive, you may be able to remedy problems by reconfiguring and reevaluating the trust, as described in [`Configuring a Trust`](configuring-a-trust.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/discovering-why-a-trust-evaluation-failed)*