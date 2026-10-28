# quadrature_integrate

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Computes an approximation to the definite integral of a function on a specified interval.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
extern double quadrature_integrate(const quadrature_integrate_function *__f, double __a, double __b, const quadrature_integrate_options *options, quadrature_status *status, double *abs_error, size_t workspace_size, void * restrictworkspace);
```

## Return Value

The function returns the result of the quadrature operation, of type `double`.

## Discussion

It also stores the status in the variable whose address was passed as the `status` parameter. The defined status constants are:

- `QUADRATURE_SUCCESS` = 0: Success.
- `QUADRATURE_ERROR` = -1: Generic error.
- `QUADRATURE_INVALID_ARG_ERROR` = -2: Invalid argument.
- `QUADRATURE_ALLOC_ERROR` = -3: Memory allocation failed.
- `QUADRATURE_INTERNAL_ERROR` = -99: This is a bug in the Quadrature code, please file a bug report.
- `QUADRATURE_INTEGRATE_MAX_EVAL_ERROR` = -101: The requested accuracy limit could not be reached with the allowed number of evals/subdivisions.
- `QUADRATURE_INTEGRATE_BAD_BEHAVIOUR_ERROR` = -102: Extremely bad integrand behavior, or excessive roundoff error occurs at some points of the integration interval.

## Discussion

On success, the absolute difference between the result *S* and the mathematically exact definite integral is assumed to be less than max(abs_tolerance, rel_tolerance * abs(*S*)).

The integration algorithms will identify *most* cases of divergence, slow convergence, and bad behavior, and report an error. You should always check the returned status and absolute error before assuming that the result is valid.

## Parameters

- `__f`: Pointer to a struct of type `quadrature_integrate_function`, defined in `integration.h`. The struct contains a pointer to the integration callback described in the previous chapter, and a pointer that will be passed as the first parameter to the integration callback
- `__a`: Value of type *double* for the first bound of the integration interval; need not be <= `__b`. If the chosen algorithm is QAGS, this may be `+INFINITY` or `-INFINITY`.
- `__b`: Value of type *double* for the second bound of the integration interval; need not be >= `__a`. If the chosen algorithm is QAGS, this may be `+INFINITY` or `-INFINITY`.
- `options`: Pointer to a struct of type `quadrature_integrate_options`, defined in `integration.h`. The integration options control the logic of the integration as described in the previous chapter.
- `status`: Pointer to a variable of type `quadrature_status`, an enum type defined in `Quadrature.h`, or `NULL`. If not `NULL`, the variable will contain the status of the integration after the function returns. The defined values for the status are given below under “Return value.”
- `abs_error`: Pointer to a variable of type `double`, or `NULL`. If not `NULL`, the variable will contain the estimated absolute error in the result after the function returns.
- `workspace_size`: Value of type `size_t`; the size of the workspace you are supplying. Ignored if you are not supplying a workspace.
- `workspace`: Pointer to a workspace area you have allocated, or NULL.

## See Also

### Quadrature
- [struct quadrature_integrator](./quadrature_integrator.md)
  Constants that specify integration algorithms.
- [struct quadrature_status](./quadrature_status.md)
  Constants that indicate the status of a quadrature operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/quadrature_integrate)*